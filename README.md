# CSC 426 Project

Contributors:

[Jarrod Carson](https://github.com/JarrodCarson) [jmc1627@jagmail.southalabama.edu]\
[Trinity Stroud](https://github.com/trinity-stroud) [tls1627@jagmail.southalabama.edu]

## Project Summary

### Problem Statement

The purpose of this proposed project is to make use of association mining of Twitter posts in order to detect and determine the scope and reach of natural disasters such as hurricanes and tropical storms.

### Dataset

The dataset being used for this project is an archived, shallow collection of JSON taken from the general Twitter stream from March 1, 2020. This information was made available by the [Archive Team: The Twitter Stream Grab](https://archive.org/details/twitterstream) at the [Internet Archive](https://archive.org/index.php). The data attributes of interest to our project include:


| Data Attribute | Description |
| --- | --- |
| created_at | The UTC time at which the Tweet was created |
| text | The UTF-8 text of the Tweet, containing the message content |
| in_reply_to_status_id_str | The id of the Tweet a status update is in reply to, if available |
| user.location | The location of the user who posted a particular Tweet |
| coordinates | The geographical location (encoded using the geoJSON format) of the user when the Tweet was posted |
| place | Includes more detailed info about the Tweet’s post location |
| quoted_status | Contains info about the Tweet being quoted, if available |
| entities | Includes entities that have been parsed out of the text of a Tweet, such as hashtags and media |
| extended_entities | Contains an array of media metadata |
| lang | Indicates the BCP 47 language identifier associated with the Tweet’s text |
| matching_rules | Includes info associated with the rule that matched the Tweet |

### Challenges Addressed

Our proposed project addresses the challenges of processing and categorizing Twitter stream posts for information of interest related to natural disasters. An added challenge would be the ability to infer from these and related posts (i.e., shared, quoted, replied to) data such as the severity of damage and reach of impact of these natural disasters.

### Project Significance

This project is significant for its potential to aid professionals and volunteers in relief efforts for areas affected by natural disasters. With the ability to monitor the direction of and devastation wreaked by hurricanes, tropical storms, etc. comes the ability to warn areas projected to be affected and direct relief efforts to already affected areas. This form of observation, projection, and communication would be a useful process for minimizing loss due to natural disasters.

### Methodology

This project will utilize the Python scripting language as a platform to perform association mining of Twitter data. This will involve analyzing particular data fields of interest within Tweet objects, mainly the text post of the Tweet, to determine if, where, and when a natural disaster is occurring. The project will make use of processing libraries such as Pandas for data manipulation in addition to a SQL Server database to facilitate the handling of data.

### Expected Results

The results are expected to be displayed as a collection of points on a map corresponding to geographical locations of reported incidents of damage according to location data in Twitter posts. Using software such as Tableau, we can visually graph observed data for specific periods of time and, using calculations to project targeted areas, we can also depict the projected direction and movement of natural disasters.

### Project Novelty

The novelty of this solution comes from the proposed ability to predict and depict data visually from Twitter data related to weather related catastrophe. To confirm the success of our project, we will manually cross-reference our graphical results with observed, historical meteorological and geological reports. We expect to be able to complete major portions of our project within the set timeframe, if not the entirety of our proposed project.