import boto3
from pprint import pprint
from credentials import aws_access_key_id, aws_secret_access_key

def detectText(photo, bucket):
    client=boto3.client('rekognition', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    textDetections=response['TextDetections']
    detectLineAndWord(textDetections)
    '''
    print ('Detected text\n----------')
    for text in textDetections:
            print ('Detected text:' + text['DetectedText'])
            print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            print ('Id: {}'.format(text['Id']))
            if 'ParentId' in text:
                print ('Parent Id: {}'.format(text['ParentId']))
            print ('Type:' + text['Type'])
            print()
    '''
    return len(textDetections)


def detectLineAndWord(textDetections):
    detected_lines = []
    detected_words = []

    for text in textDetections:
      if text['Type'] == 'LINE':
        dict_copy = text.copy()
        detected_lines.append(dict_copy)
      elif text['Type'] == 'WORD':
        dict_copy = text.copy()
        detected_words.append(dict_copy)
      else:
        continue

    pprint(detected_lines)
    pprint(detected_words)
    print("Lines detected: " + str(len(detected_lines)))
    print("Words detected: " + str(len(detected_words)))


def main():
    bucket='ss-expr'
    photo='bill.jpeg'
    text_count=detectText(photo,bucket)
    print("Text detected: " + str(text_count))


if __name__ == "__main__":
    main()
