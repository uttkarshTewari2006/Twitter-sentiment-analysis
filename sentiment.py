import kagglehub
import pandas

# Download latest version
path = kagglehub.dataset_download("abhi8923shriv/sentiment-analysis-dataset")

print("Path to dataset files:", path)


train_data = pandas.read_csv(path + "/train.csv", encoding='latin-1')
test_data = pandas.read_csv(path + "/test.csv", encoding='latin-1')

train_data.info()
train_data.head()