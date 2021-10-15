import boto3


class S3(object):

    def __init__(self, file_name: str):
        self.__client = boto3.client("s3")
        self.__resources = boto3.resource("s3")
        self.__bucket_name = "data-eng-resources"
        self.__object = self.__client.get_object(Bucket=self.__bucket_name, Key=f"python/{file_name}")


    def get_client(self):
        return self.__client

    def get_resources(self):
        return self.__resources

    def get_object(self):
        return self.__object

    def get_bucket_name(self):
        return self.__bucket_name

    def get_key_name(self):
        return self.__key_name

    def get_object_body(self):
        return self.get_object()["Body"]

