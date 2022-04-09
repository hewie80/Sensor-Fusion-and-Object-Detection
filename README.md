# Final Project Sensor-Fusion-and-Object-Detection
# Write a short recap of the four tracking steps and what you implemented there (EKF, track management, data association, camera-lidar sensor fusion). Which results did you achieve? Which part of the project was most difficult for you to complete, and why?
EKF: It includes two parts. One is prediction and the other is update. Based on initialzied track, EKF predict new track. And updated the new track with new measurement. It exports predicted track status and uncertainty covariance. 
Track management: It is used to initialize new track, delete old tracks of low track score under the threhold and assign some confidence value to tracks. 
Association: With SNN, calculates all Mahalanobis distances between tracks and measurements, then iteratively updates the closest association pair.
Camera-lidar sensor fusion:  Updates all tracks with lidar measurements, then with camera measurements. 
Association is the most diffcult for me. The logic is hard for to understand. And also the code is long and take me much time to finish. 
# Do you see any benefits in camera-lidar fusion compared to lidar-only tracking (in theory and in your concrete results)?
Theory: More sensor means more measurement. It contribute more accurancy based on Kalman Filter. 
Concrete results: RMSE value decreased and the accuracy increased after more sensor is used.
![Step4 RMSE](https://user-images.githubusercontent.com/99339837/162555665-35af746e-0c0a-41b0-9c33-d36528168771.png)

# Which challenges will a sensor fusion system face in real-life scenarios? Did you see any of these challenges in the project?
False detect. Below picture is captured from the project. Arbuscle is identified as car. which maybe cause sudden brake.
![image](https://user-images.githubusercontent.com/99339837/162555794-57fd6738-8c78-4782-afd6-5baff768d43a.png)

# Can you think of ways to improve your tracking results in the future?
More sensors bring more accurancy. But it also brings more calculation. which will bring more power consumption of car. For EV car, that will sacriface the mileage。
so my first thinking is to imporve the capablity of Lidar or camera so as to reduce fusion as less as possible. e.g camera is good at classfication, 2D-structure, dimension and velocity. but poor at distance measurement, bad environment such as darknees,foggy, rainny and so on. It is possible to improve ability of distance measurement by updated algorithm. In bad enviroment, use Infrared measurement technology to improve the capbilty of camera in darkness. 
