# seconds-worked

This module helps you calculate seconds in a working day with two given ISO format times.
This project provides an easy way to calculate the total number of business seconds between two given times.
A business second is defined as any whole second that elapses after 08:00 and before 17:00 during a weekday 
(Monday - Friday), that is not a public holiday in the Republic of South Africa.
The module accepts only two required parameters: start_time and end_time and optional parameter date.
The date parameter defaults to today's date if the date is not provided.
Parameter values will be in ISO-8601 format. It returns only a single integer value or a suitable error message string 
for failed requests.
