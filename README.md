# AirlinesReview
### British Airlines Review

Many companies rely on the reviews on their website or the third-party website to understand their customers's feedback for their products and services. British Airways offers the virtual internship opportunity which is on The Forage to let students or anyone who is interested in data analytics or data science to get the idea of what data scientist at British Airways is working. Their virtual internship program provides two tasks. The first one scraping customers' review on the third-party website (Skytrax) and then do some analysis such as sentiment analysis, topic modelling and word cloud to help company understand customers' opinion currently. The second task is using machine learning to build a predict model for customers' purchase behaviors with provided dataset. 

In this post, I cover the first task. Even though the task requires some particular things, I think it would be fun to play around with the data collected from Skytrax not only for British Airways but also for other airlines if they would love to know more about their customer's feedback and learn from those to improve their products and services. With the power of Large Language Model (LLM), I also think it is possible to build an application that assists airlines answer their customer's feedback and provide the summarization for airlines's manager, leader to know which areas of the services need to be improved and have the better decisions or strategy to serve their customers better. 

Below is the analysis from British Airways review. However, the code provided can be used to scrape reviews from any airlines on Skytrax. 

Skytrax collects customer's experience with the review in text but also allows customers to rate different metrics that are important to evaluate the good flight such as the seat comfort, cabin staff service, food & beverages, entertainment, ground services... These metrics if aggregated can help us have the bigger picture of how well the airline is doing for each category, learn the one that performs poorly, investigate the behind reasons and have the appropriate actions to immediately tackle them. 
According to the collected data, British Airways is rated 1 for many categories: overall rating which indicates the overall experiences of customers, food and beverages, inflight entertainment, ground service, wifi & connectivity, value for money. Most of their customers said that they would not recommend their airlines for their family or friends. However, their cabin staff servie and seat comfort are highly valued by customers. 

### Word Cloud and Sentiment Analysis
While the word cloud of all rating shows us the topic that BA customers are the most concerned, the word cloud of negative reviews gives us the pictures of the topics that are most discussed, usually complaints and the request to change the service. Along with some categories that are rated badly above, food drink, time, sear, are discussed the most. It seems like customers expect more services and hostipility from the airways on their flight. 

Apply the sentiment package from TextPlot, the distribution of the reviews after analyzing sentiment is normal distribution. While there are a lot of 1 rating from customers, the text reviews show the customers don't use very strong words to BA services and flights. There are a few of reviews which are strongly positive or strongly negative.  

Since first class is also discussed a lot, let me investigate the average rating from the seat type to see if there any differences from customers feedback according to the seat type that customers choose. 

### Future work
There are different things that we can do as data scientist to assist the company with their services to their customers
1. Using LLM to build an application to build the automatic bot to acknowledge customers' concerns, feedback so that the customers feel like they are heard. 
2. Summarizing reviews weekly, monthly, quarterly and yearly so that the company have a good picture for any strategic changes. 
3. Build an website for review scraping and basic analysis for any airlines.
