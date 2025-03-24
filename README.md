# **Analysis Report: Airbnb Listings in New York**
![Header Image](https://vissaihotel.vn/photo/airbnb-la-gi1.jpg)  
---

## **Introduction**
This report presents the results of an in-depth analysis of Airbnb listings in New York. The goal of this analysis was to uncover key insights about pricing, distribution, and customer behavior to help stakeholders make data-driven decisions. The dataset includes information such as price, room type, location, number of reviews, and availability.

---

## **Key Insights**

### **1. Price Distribution**
- **Insight**: The majority of Airbnb listings in New York are priced between **$0 and $200**, with very few listings exceeding **$500**.
- **Implication**: Affordable listings dominate the market, suggesting that budget-friendly options are in high demand.

*Figure 1: Distribution of Airbnb listing prices.*

---

### **2. Room Type Distribution**
- **Insight**: The most common room types are **Entire Home/Apt** and **Private Room**, while **Shared Rooms** are significantly less common.
- **Implication**: Travelers prefer privacy and space, making entire homes and private rooms more attractive.

*Figure 2: Distribution of room types.*

---

### **3. Geographical Distribution**
- **Insight**: Listings are concentrated in **Manhattan** and **Brooklyn**, with fewer listings in other boroughs like **Queens** and **Staten Island**.
- **Implication**: Manhattan and Brooklyn are the most popular areas for Airbnb listings, likely due to their proximity to tourist attractions and business hubs.

*Figure 3: Geographical distribution of Airbnb listings.*

---

### **4. Relationship Between Price and Number of Reviews**
- **Insight**: There is a **negative correlation** between price and the number of reviews. Lower-priced listings tend to have more reviews.
- **Implication**: Affordable listings are more frequently booked and reviewed, indicating higher customer engagement.

*Figure 4: Relationship between price and number of reviews.*

---

### **5. Top Hosts with Most Listings**
- **Insight**: A small number of hosts manage a large portion of the listings. For example, the top 10 hosts account for a significant share of the market.
- **Implication**: These hosts may have a competitive advantage due to their scale and experience.

*Figure 5: Top hosts with the most listings.*

---

### **6. Availability Over 365 Days**
- **Insight**: Most listings are available for more than **200 days a year**, with some listings available year-round.
- **Implication**: High availability suggests that hosts are actively renting out their properties, but it may also indicate oversupply in certain areas.

*Figure 6: Distribution of availability over 365 days.*

---

### **7. Relationship Between Minimum Nights and Price**
- **Insight**: Listings with higher minimum night requirements tend to have **higher prices**.
- **Implication**: Hosts may be targeting longer-term stays, which could appeal to business travelers or families.

*Figure 7: Relationship between minimum nights and price.*

---

### **8. Number of Reviews Over Time**
- **Insight**: The number of reviews has been increasing over time, with noticeable spikes during peak travel seasons.
- **Implication**: Airbnb usage is growing, and customer engagement is highest during specific periods of the year.

*Figure 8: Number of reviews over time.*

---

### **9. Correlation Matrix**
- **Insight**: There is a **weak negative correlation** between price and the number of reviews, and a **positive correlation** between availability and the number of reviews.
- **Implication**: Lower-priced and highly available listings tend to attract more reviews and bookings.

*Figure 9: Correlation matrix of key variables.*

---

### **10. Average Price by Neighbourhood Group**
- **Insight**: **Manhattan** has the highest average price, followed by **Brooklyn**. Other boroughs like **Queens** and **Staten Island** are more affordable.
- **Implication**: Manhattan and Brooklyn are premium markets, while other areas offer more budget-friendly options.

*Figure 10: Average price by neighbourhood group.*

---

## **Linear Regression Analysis**
To predict **price** based on the **number of reviews**, a simple linear regression model was built. The results are as follows:
- **Regression Coefficients**:
  - Intercept (`beta_0`): **154.32**
  - Slope (`beta_1`): **-0.19**
- **Mean Squared Error (MSE)**: **51088.91**

### **Interpretation**:
- The negative slope indicates that as the number of reviews increases, the price tends to decrease.
- The high MSE suggests that the model has room for improvement, possibly by including additional features like room type or location.

*Figure 11: Linear regression of price vs number of reviews.*

---

## **Recommendations**
1. **Focus on Affordable Listings**: Since lower-priced listings receive more reviews and bookings, hosts should consider competitive pricing strategies.
2. **Target High-Demand Areas**: Manhattan and Brooklyn are the most popular areas. Hosts in these regions should optimize their listings to attract more guests.
3. **Encourage Longer Stays**: Listings with higher minimum night requirements tend to have higher prices. Hosts can target business travelers or families by offering discounts for longer stays.
4. **Improve Availability**: Listings with high availability receive more reviews. Hosts should ensure their properties are available during peak travel seasons.
5. **Enhance Model Accuracy**: Future analyses should include additional features like room type, location, and amenities to improve the predictive power of the regression model.

---

## **Conclusion**
This analysis provides valuable insights into the Airbnb market in New York. By understanding pricing trends, customer preferences, and geographical distribution, stakeholders can make informed decisions to optimize their listings and maximize revenue. The linear regression model, while simple, highlights the importance of considering multiple factors when predicting prices.

---

**Prepared by**: Amirhossein Ojaghi  
**Date**: Monday, March 24, 2025  
🔗 [GitHub](https://github.com/AH-ojaghi/Airbnb-listing-analysis-in-New-York)<br>
🔗 [Email](www.aojaghi036@gmail.com)

--- 
