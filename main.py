import pandas as pd
from pandas import read_pickle
from matplotlib import pyplot as plt
from os import path
import re

# GLOBAL VARIABLES / USER INPUT VARIABLES.


# path to access the histroy JSON file
historyPath = "watch-history.json"

# Name of the file you want to create to view your favorite channels.

mostViewedVideos = "Most Viewed Videos"

channelDataFrame = "Channel Data Frame"





def urlToID(url):

    value = url.split('=')
    return value[1]

def createDF(filename):

    if (path.exists(filename)):
        return read_pickle(filename)
    else:
        df = jsonToData(historyPath)
        # converts json file to pandas data frame
        df.to_pickle(filename)
        return read_pickle(filename)

def favoriteChannel(df):

    df['subtitles'].value_counts().to_csv("Favorite Channel.csv", sep = ",")

def plotFavoriteChannel(df, number = 10):

    newdf = df['subtitles'].value_counts()


    stringre = r"(?<=\{\'name\': \')(.*)(?=\',)"
    string_pattern = re.findall(stringre, str(newdf[:number]))

    string_pattern = string_pattern[0:number]
    print(len(string_pattern))

    fig, ax = plt.subplots()
    fig.canvas.draw()

    newdf.iloc[0:number].plot(kind="bar")
    labels = string_pattern
    ax.set_xticklabels(labels)
    plt.show()


def mostWatchedVideo(df):
    runningValue = 0
    df['title'].value_counts().to_csv(mostViewedVideos)
    runningValue = df['title'].value_counts()
    json_file = open(historyPath, encoding="UTF8")
    print("Number of Videos Included: ", f'{len(df):,}')

def jsonToData(historyPath):
    data = pd.read_json(historyPath)
    df = pd.DataFrame(data)
    df = df.dropna()
    df.to_csv("Raw Data")
    return df
def saveAsDataFrame(fileName, histroyPath):
    if (path.exists(fileName)):
        return read_pickle(fileName)
    else:
        df = jsonToData(historyPath)
        df.to_pickle(fileName)
        return read_pickle(fileName)

def main():


    df = createDF(channelDataFrame)
    mostWatchedVideo(df)
    favoriteChannel(df)
    plotFavoriteChannel(df, 10)

if __name__ == "__main__":
    main()


