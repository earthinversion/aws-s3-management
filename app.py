from flask import Flask, render_template, request, redirect, url_for, flash, Response, session
from flask_bootstrap import Bootstrap
from resources import aws_bucket_info, get_bucket_list
from config import port
from filters import datetimeformat, file_type

# s3 = boto3.client('s3',aws_access_key_id=S3_KEY,aws_secret_access_key=S3_SECRET)




app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'secret'
app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['file_type'] = file_type

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        bucket = request.form['bucket']
        session['bucket'] = bucket
        return redirect(url_for('data'))
    else:
        buckets = get_bucket_list()
        return render_template('index.html', buckets=buckets)

@app.route('/data')
def data():
    my_bucket = aws_bucket_info()
    summaries = my_bucket.objects.all()
    return render_template('data.html',my_bucket=my_bucket, files = summaries )

@app.route('/upload', methods = ['POST'])
def upload():
    file = request.files['file']

    my_bucket= aws_bucket_info()
    my_bucket.Object(file.filename).put(Body=file)
    flash('File uploaded successfully')
    return redirect(url_for('data'))

@app.route('/delete', methods = ['POST'])
def delete():
    key = request.form['key']
    my_bucket= aws_bucket_info()
    my_bucket.Object(key).delete()
    flash('File deleted successfully')
    return redirect(url_for('data'))

@app.route('/download', methods = ['POST'])
def download():
    key = request.form['key']
    my_bucket= aws_bucket_info()
    file_obj = my_bucket.Object(key).get()

    return Response(
        file_obj['Body'].read(),
        mimetype = 'text/plain',
        headers = {'Content-Disposition': 'attachment;filename={}'.format(key)}
    )



if __name__=="__main__":
    # app.run(port=port, debug=True)
    app.run(port=port, debug=False)