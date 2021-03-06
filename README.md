# WeatherAPI

Welcome to the weather API! This is a tech evaluation by Globant where you have an API that tells you the current weather in your city and country.

The API was built with <3 using FastAPI and connected to an AWS database instance. 

To run the program, you need to follow the following steps:

First, you have to clone this repo using the "git clone" command:

```git clone repo_url```

using the url provided by GitHub. Alternatively, you can download the repo in a .zip file.

After you have successfully downloaded the repository, you have to install all the requirements in the requirements.txt file by opening a Command Line Interface and navigate where the repo is located. Then you need to run the following command:

```pip install -r requirements.txt```

You are almost all set! The last thing you need to do is run the command to start the server:

```uvicorn main:app --reload```

This is going to initialize the local server (127.0.0.1) in the port 8000.

You can access the current weather in your zone by providing the variables (via the GET method) in the following format:

```'city' = 'La Plata'```
```'country' = 'AR'```

That is if, for example, you live in La Plata, Argentina. These values are strings.

This is how the previous URL would look like if you want to check the actual JSON:

```http://127.0.0.1:8000/weather?city=La%20Plata&country=AR```

But there's more to it! If you go to:

```http://127.0.0.1:8000/docs```

you will access a Swagger-based app where you will be able to test the endpoint and check the response and the data!

You can try experimenting with cities all around the world!

A brief note: The app uses a string-type environment variable for the api key that you need to declare to override mine (under the name ```api_key```) to be able to use the API provided by OpenWeatherMap.org and it can be obtained by registering for free, it will be active after approximately 30 minutes after you request it.