# GigShield AI – Parametric Insurance for Gig Workers

## Problem
Gig delivery workers working for platforms like Zepto, Swiggy, and Amazon depend on daily earnings. When disruptions such as heavy rain, extreme heat, floods, or pollution occur, deliveries stop and workers lose income. Currently, there is no protection for such income loss.

## Solution
GigShield AI is an AI-powered parametric insurance platform that automatically compensates gig workers for income lost due to external disruptions.

The system:
- Calculates weekly premiums using AI risk prediction
- Monitors disruption triggers (weather, pollution)
- Automatically triggers claims
- Instantly pays compensation

## Persona
Quick commerce delivery workers (Zepto, Blinkit, Instamart).

Example worker:
Name: Rahul  
City: Hyderabad  
Weekly income: ₹4000

## Weekly Pricing Model
Workers pay a small weekly premium.

Example:
Weekly income: ₹4000  
Premium: ₹25/week  
Coverage: ₹200 per disruption day  
Maximum payout: ₹1000/week

## Parametric Triggers
Heavy Rain (>40mm rainfall)  
Extreme Heat (>42°C)  
High Pollution (AQI >300)

## AI Integration
AI is used for:
- Risk prediction
- Dynamic premium calculation
- Fraud detection

Model inputs:
- Weather data
- AQI
- Location
- Historical disruptions

Algorithm:
Random Forest Regression

## Platform Choice
Web platform (React + Node.js) to allow easy access and faster development.

## Tech Stack
Frontend: React  
Backend: Node.js  
Database: PostgreSQL  
AI: Python + Scikit-learn  
APIs: OpenWeather API, AQI API  
Payments: Razorpay Test Mode

## Workflow
1. Worker registers
2. AI calculates risk score
3. Weekly policy created
4. APIs monitor disruptions
5. Claims triggered automatically
6. Instant payout

## Development Plan
Week 1-2: Research + Prototype  
Week 3-4: Automation & Claims  
Week 5-6: Fraud detection + Dashboard

## Future Features
- AI fraud detection
- Risk heatmap
- Instant payout system
- Analytics dashboard
