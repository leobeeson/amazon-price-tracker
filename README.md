# Amazon Price Tracker

## Behaviour
1. Decide which product in Amazon you'd like to set up a price tracker and grab its URL.
2. In main.py, replace the values for the arguments:
    * PRODUCT_NAME: Give the product a meaningful name to you.
    * PRODUCT_URL: Add the product's Amazon URL.
    * DESIRED_PRICE: Maximum price you'd like to pay for this product.
    * NOTIFICATION_EMAIL: Email where you want to be notified, if the the product drops below DESIRED_PRICE.
    * NOTIFICATION_FREQUENCY: How often you want the product to be checked on Amazon.
        * Default = 1 day (i.e. 86,400 seconds)
3. An email will be sent to `NOTIFICATION_EMAIL` every `NOTIFICATION_FREQUENCY` if `PRODUCT_NAME` drops below `DESIRED_PRICE`.

## Requirements
1. Create a new Gmail account (I highly recommend not using a personal email for sending these notifications).
2. Set up an App Password to your newly created Gmail account.
    * How to set up App Password on Gmail:
        * This video shows [how to set up App Password](https://www.youtube.com/watch?v=BFTCVC33qhQ&t=374s).
        * Google's [formal instructions](https://support.google.com/accounts/answer/185833) for setting up an App Password.
3. Create a file called `.env` in your project's root folder, and add the following variables:
    ```txt
    GMAIL_TEST_USER={your newly created email address}
    APP_PASSWORD={app password generated in the step above}
    ```
4. Find your HTTP request headers. 
    1. Browse to `http://myhttpheader.com/` and it'll show you the specific HTTP request headers you should use for sending requests from your machine.
    2. Create a file called `request_headers.json` in your project's root folder, and add the HTTP headers for at least `User-Agent`, `Accept-Language`, and `Accept`, such as:
        ```json
        {
        "User-Agent": "Mozilla/5.0 ...",
        "Accept-Language": "en-US ...",
        "Accept": "text/html ..."
        }
        ```
5. Run `python3 main.py` (or `python main.py` if on Windows with no Python2).

## Improvements
* For simplicity, the program is running on an eternal loop with a day-long `sleep` call to check for the product's price once a day.
* For running the program locally or on a remote server, an improvement would be to call the main.py script using a [cron job](https://gavinwiener.medium.com/how-to-schedule-a-python-script-cron-job-dea6cbf69f4e) (or [Task Scheduler](https://datatofish.com/python-script-windows-scheduler/) on Windows):
    1. Remove the `sleep` call and the `NOTIFICATION_FREQUENCY` variable, as they will no longer be necessary.
    2. Set up the crontab, e.g. to run every day at midnight (make sure to change the path to the python3 executable and the script location to your specific locations):
        ```crontab
        0 0 * * * /usr/bin/python3 /home/%USER%/path/to/project/main.py >> ~/cron.log 2>&1
        ```
* For a cloud infrastructure approach, an improvement would be to run the application using AWS Lambda:
    1. Convert the main.py script into a [Python Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html).
    2. Deploy Python Lambda function with [dependencies as a .zip file archive](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html).

## Caution:
### Gmail App Password
- Take care of the `app password` provided by Gmail; keep it in the `env` file or some other non-git-commitable configuration file. Again, preferably set up a separate Gmail account just for this service, and avoid using your personal email account.
- The current `.env` is currently included in the `.gitignore` file; avoid removing it from it.
- The `request_headers.json` file with your HTTP request headers is also currently included in the `.gitignore` file. It's not the end of the world if you commit them, but some people have privacy concerns with them, and more importantly, anyone cloning your code will have to set their own anyways.

## Credits:
- This project was motivated by the [Day 47 project](https://www.udemy.com/course/100-days-of-code/learn/lecture/21839858#questions/17098568), from the course [100 Days of Code: The Complete Python Pro Bootcamp for 2022](https://www.udemy.com/course/100-days-of-code/learn/).