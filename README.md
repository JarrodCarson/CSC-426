# The Use of Frequency Analysis of Twitter Data to Detect Natural Disasters

Contributors:

[Jarrod Carson](https://github.com/JarrodCarson) [jmc1627@jagmail.southalabama.edu]\
[Trinity Stroud](https://github.com/trinity-stroud) [tls1627@jagmail.southalabama.edu]

## Project Summary

### Problem Statement

The purpose of this proposed project is to make use of frequency analysis of Twitter posts in order to detect and determine the scope and reach of natural disasters such as hurricanes and tropical storms.

### Dataset

The dataset being used for this project is an archived, shallow collection of JSON taken from the general Twitter stream from March 1, 2020. This information was made available by the [Archive Team: The Twitter Stream Grab](https://archive.org/details/twitterstream) at the [Internet Archive](https://archive.org/index.php). The link to download this dataset can be found [here](https://archive.org/download/archiveteam-twitter-stream-2020-03/twitter_stream_2020_03_01.tar).

### Challenges Addressed

Our proposed project addresses the challenges of processing and categorizing Twitter stream posts for information of interest related to natural disasters. An added challenge would be the ability to infer from these and related posts (i.e., shared, quoted, replied to) data such as the severity of damage and reach of impact of these natural disasters.

### Project Significance

This project is significant for its potential to aid professionals and volunteers in relief efforts for areas affected by natural disasters. With the ability to monitor the direction of and devastation wreaked by hurricanes, tropical storms, etc. comes the ability to warn areas projected to be affected and direct relief efforts to already affected areas. This form of observation, projection, and communication would be a useful process for minimizing loss due to natural disasters. This project is a first step to reaching this goal.

### Methodology

This project will utilize the Python scripting language as a platform to perform frequency analysis of Twitter data. This will involve analyzing particular data fields of interest within Tweet objects, mainly the text post of the Tweet, to determine if, where, and when a natural disaster is occurring. The project will make use of libraries such as json, bz2, and os for data manipulation and file management.


## Data Preparation

### Dataset

The dataset used in this project is the [March 1, 2020 Twitter Stream](https://archive.org/download/archiveteam-twitter-stream-2020-03/twitter_stream_2020_03_01.tar) collected by the [Twitter Stream Grab Archive Team](https://archive.org/details/twitterstream) and hosted at the [Internet Archive](https://archive.org/index.php).

This Twitter Stream is a collection stored as a .tar file, within which are 24 directories for each hour of the day. Each hour directory has 60 files for each minute of each hour, these files being compressed JSON files of Tweet objects. The .tar file is itself 2.2 GB, but uncompressed all of the files together amount to about 22 GB.

### Feature Selection

Though Tweet objects contain many useful and informative fields, the only ones of interest to our project are the following Tweet object attributes:

| Data Attribute | Description |
| --- | --- |
| coordinates | The geographical location (encoded using the geoJSON format) of the user when the Tweet was posted |
| created_at | The UTC time at which the Tweet was created |
| entities | Includes entities that have been parsed out of the text of a Tweet, such as hashtags and media |
| extended_entities | Contains an array of media metadata |
| in_reply_to_status_id_str | The id of the Tweet a status update is in reply to, if available |
| lang | Indicates the BCP 47 language identifier associated with the Tweet's text  |
| place | Includes more detailed info about the Tweet’s post location |
| quoted_status | Contains info about the Tweet being quoted, if available |
| text | The UTF-8 text of the Tweet, containing the message content |
| user | The user who posted the Tweet|

We chose these attributes to track information such as the location at which a Tweet was posted, the time at which a Tweet was posted, the text of a Tweet, and the language in which a Tweet was written. Other attributes, such as `quoted_status` and `in_reply_to_status_id_str`, allow us to see relationships between different Tweets, whether a Tweet was written in reply to or quoting another Tweet. Collecting this information is useful for the purposes of drawing relationships between time, location, and content of Tweets for characterizing Tweets made in reference to natural disasters and then plotting those Tweets by geography and time.

For a complete list of Tweet object attributes and their descriptions, visit the following [website](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/tweet-object).
