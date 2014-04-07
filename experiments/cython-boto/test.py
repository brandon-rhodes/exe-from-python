# Needs environment variables:
# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY

import boto

def main():
    conn = boto.connect_s3()
    bucket = conn.create_bucket('jplephem')
    for item in bucket.list():
        print(item.name)

if __name__ == '__main__':
    main()
