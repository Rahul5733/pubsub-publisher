# pubsub-publisher knowledge base


![Alt text](images/bf_logo.jpg?raw=true "Title")

&emsp;
&emsp;
***“Torture the data, and it will confess to anything.” — Ronald Coase***

**How to run this publisher**
---
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

Here is an example, How to randomize message keys, Here your keys are added to the list and 

```
    keys_to_randomize = {
        "pipelineComponent": gen_random_string(),
        "pipelineName": gen_random_string(),
        "timestampStart": gen_random_date(),
        "timestampStop": gen_random_date(),
        "randomNumber": gen_random_number(),
    }
```

**Usefull information about pubsub-publisher**
---
1. For starters, an introduction about pubsub-publisher components

    https://medium.com/swlh/apache-pubsub-publisher-in-5-minutes-c005b4b11b26

2. How Big companies are using pubsub-publisher

    https://www.youtube.com/watch?v=428AiCBMZoQ


3. pubsub-publisher documentation

    https://pubsub-publisher.apache.org/docs/apache-pubsub-publisher/stable/tutorial.html
 
