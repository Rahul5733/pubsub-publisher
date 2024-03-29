
&emsp;
&emsp;
***“Torture the data, and it will confess to anything.” — Ronald Coase***


# pubsub-publisher
This service can be used as a simulator for pubsub message publisher, it can:
- Send messages to pubsub topic as batch or stream data
- Randomize keys in the message so that every message sent is different
- Vary the size and frequency of message stream/batches

**How to run this publisher**
---


1. Clone this repo, using:

    `git clone https://github.com/Blueforte-GmbH/pubsub-publisher.git`

2. move into the clonned repo:

    `cd pubsub-publisher`

3. Install, create and activate the python virtual environment
    ```
    sudo apt install python3-virtualenv (if not yet installed)

    virtualenv venv

    source venv/bin/activate (in Windows: <current_environment_folder>: Scripts\activate
                              in Unix: <current_environment_folder>: source Scripts/activate)
    ```
4. Install pubsub-publisher using pip
    ```
    pip3 install -r requirements.txt

    ```
5. That's it, pubsub-publisher is installed, create a service account and allot it the required credentials, store the key file somewhere locally
    The key file must be named 'pubsub-sa.json' (because that's its name in .gitignore) and has the following structure:
    ```
    {
    "client_id": "",
    "client_secret": "",
    "quota_project_id": "",
    "refresh_token": "",
    "type": ""
    }
    ```
    This file is usually created when running the command 'gcloud auth application-default login'
    and is located in your gcloud folder.

5. Now change the config.yaml file with your project settings
    ```
    projectId: YOUR_PROJECT_ID
    topicPath: projects/PROJECT_ID/topics/TOPIC_NAME
    subscriptionPath: "paste the subscription path here"
    credentialsPath: PATH-TO-THE-CREDENTIALS-FILE
    ./run_publisher.sh
    ```
    This file should be put in .gitignore to not accidentally publish credentials to Git.

6. in case, the subscription has to be emptied, empty it using
    ```
    ./empty_subscription.sh
    ```

**How to run locally and on the cloud**
 to run locally, just uncomment the code line in [publisher.py](src/publisher.py):

 `os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path`

 (if not working, login using 'gcloud auth application-default login' once to change
 the file 'application_default_credentials.json' in your gcloud folder and comment out the line above)

 to run it in the cloud, comment it out:

 `# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path`

 **How to change message config**

 [config](config.yaml) file has the parameters which can be tweaked to change the behavior of this publisher.

``` numberOfMessages: 15 (Number of messages to be sent)
messageArgs:(can be used to filter messages)
    origin: python-sample 
    username: GCP
batch: False (when set to 'true'), messages will be sent in batches otherwise in stream
batchSettings:
    maxMessages: 100 (max number of messages to be sent in a batch)
    maxBytes: 1024  (max number of bytes to be sent in a batch)
    maxLatency: 1
```

**How to deploy on the cloud run**
clone the repo, authenticate on the GCP with your terminal, and run:

`gcloud builds submit --tag gcr.io/PROJECT_NAME/CONTAINER_REPO`

This will push the image to the cloud, Now you can simply start a cloud-run service using the GCP console or from the terminal. You need to choose the image pushed in the container registry and service accout(with all the permissions required) for it.



**How to add/remove keys in randomizer**

This can be done by editing the file [keys_to_randomize.py](src/keys_to_randomize.py)

Here is an example, How to randomize message keys, Here five example keys are added to the dict, these values will be random in every message, depending on the data type, there are three methods written for srting, datetime, and int.

For example, a key "pipelineMetricId" has to be randomized and it's an integer type, add that key to this dict and gen_random_number() as its value.

```
    keys_to_randomize = {
        "pipelineComponent": gen_random_string(),
        "pipelineName": gen_random_string(),
        "timestampStart": gen_random_date(),
        "timestampStop": gen_random_date(),
        "randomNumber": gen_random_number(),
    }
```


