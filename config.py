import os

S3_BUCKET = os.environ.get("S3_BUCKET")
S3_KEY = os.environ.get("S3_KEY")
S3_SECRET = os.environ.get("S3_SECRET")
port = int(os.getenv('PORT', 8000))

if __name__=="__main__":
    print(S3_BUCKET)
    print(S3_KEY)
    print(S3_SECRET)