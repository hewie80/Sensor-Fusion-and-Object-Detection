# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        pass

    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############
        dt=params.dt
        return np.matrix([[1,0,0,dt,0,0],
                     [0,1,0,0,dt,0],
                     [0,0,1,0,0,dt],
                     [0,0,0,1,0,0],
                     [0,0,0,0,1,0],
                     [0,0,0,0,0,1]])
      
        ############
        # END student code
        ############ 

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############
        q=params.q
        dt=params.dt
        q1 = ((dt**3)/3) * q 
        q2 = ((dt**2)/2) * q 
        q3 = dt * q 
        return np.matrix([[q3,0,0,q2,0,0],
                     [0,q3,0,0,q2,0],
                     [0,0,q3,0,0,q2],
                     [q2,0,0,q1,0,0],
                     [0,q2,0,0,q1,0],
                     [0,0,q2,0,0,q1]]) 

        ############
        # END student code
        ############ 

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############
        F = self.F()
        x=track.x
        P=track.P
        x = F*x # state prediction
        P = F*P*F.transpose() + self.Q() # covariance prediction
        track.set_x(x)
        track.set_P(P)
        return x, P
        
        ############
        # END student code
        ############ 

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############
        
        x=track.x
        H=meas.sensor.get_H(x) # measurement matrix
        gamma = self.gamma(track,meas) # residual
        P=track.P
        R=meas.R
        S = self.S(track, meas, H) 
        K = P*H.transpose()*np.linalg.inv(S) # Kalman gain
        x = x + K*gamma # state update
        I = np.identity(params.dim_state)
        P = (I - K*H) * P # covariance update
        track.set_x(x)
        track.set_P(P)
        return x, P     
 
        ############
        # END student code
        ############ 
        track.update_attributes(meas)
    
    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############
        z=meas.z
        x=track.x
        H=meas.sensor.get_H(x)
        return z - H*x
        
        ############
        # END student code
        ############ 

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############
        P=track.P
        R=meas.R
        
        return H*P*H.transpose() + R
        
        ############
        # END student code
        ############ 