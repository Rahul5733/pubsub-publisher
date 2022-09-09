
&emsp;
&emsp;
***“Torture the data, and it will confess to anything.” — Ronald Coase***


# pubsub-publisher
This service can be used as a simulator for pubsub messege publisher, it can:
- Send messages to pubsub topic as batch or stream data
- Randomize keys in the message so that every messege sent is different
- Varry the size and frequency of single messages/batches

**How to run this publisher**
---

![Alt text](images/bf_logo.jpg?raw=true "Title")

1. Clone this repo , using:

    `git clone https://github.com/Blueforte-GmbH/pubsub-publisher.git`

2. move into the clonned repo:

    `cd pubsub-publisher`

3. Install, create and activate python virtual environment
    ```
    sudo apt install python3-virtualenv

    virtualenv af_env

    source af_env/bin/activate
    ```
4. Install pubsub-publisher using pip
    ```
    pip3 install -r requirements.txt

    ```
5. Thats it, pubsub-publisher is installed, create a service account and allot it the required credentials, store the key file somewhere locally

5. Now change the config.json file with your project settings
    ```
    projectId: YOUR_PROJECT_ID
    topicPath: projects/PROJECT_ID/topics/TOPIC_NAME
    subscriptionPath: "paste the subscription path here"
    credentialsPath: PATH-TO-THE-CREDENTIALS-FILE
    ./run_publisher.sh
    ```

6. in case, the subscription has to be emptied, empty it using
    ```
    ./empty_subscription.sh
    ```

**How to add/remove keys in randomizer**

Here is an example, How to randomize message keys, Here five example keys are added to the dict, these values will be random in every message, depending on the data type, there are three methodes written for srting, datetime and int.

For example, a key "pipelineMetricId" has to be randomized and its an integer type, add that key to this dict and gen_random_number() as its value.

```
    keys_to_randomize = {
        "pipelineComponent": gen_random_string(),
        "pipelineName": gen_random_string(),
        "timestampStart": gen_random_date(),
        "timestampStop": gen_random_date(),
        "randomNumber": gen_random_number(),
    }
```


