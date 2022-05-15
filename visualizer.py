import streamlit as st
from stravarefresh import activities
import pandas as pd
from stravarefresh import update
# distance - meters
# time - seconds

update()

activities['distance'] = (activities['distance'] / 1609.34)
activities['moving_time'] = (activities['moving_time'] / 3600)
activities['elapsed_time'] = (activities['elapsed_time'] / 3600)

st.title('My Strava Metrics')


st.header('My Most Recent Activity:')
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Activity Type:", activities['type'][0])
with col2:
    st.metric("Distance (Miles)", round(activities['distance'][0], 2), round((activities['distance'][0] - activities['distance'][1]), 2))
with col3:
    st.metric("Elapsed Time (Hours)", round(activities['elapsed_time'][0], 2), round((activities['elapsed_time'][0] - activities['elapsed_time'][1]), 2))


st.header('Recent Activities - Distance and Moving Time (Miles & Hours)')
dist_data = pd.DataFrame(activities[0:10], columns = ['distance', 'moving_time'])
distance= st.bar_chart(dist_data)

st.header('Recent Activities - Elevation Gain (Feet)')
activities['total_elevation_gain'] = (activities['total_elevation_gain'] * 3.28084)
elev_data = pd.DataFrame(activities[0:10], columns = ['total_elevation_gain'])
elevation = st.bar_chart(elev_data)

lat_lng_df = activities['end_latlng']
position = pd.DataFrame(lat_lng_df)
split_df = pd.DataFrame(position['end_latlng'].tolist(),columns=['latitude', 'longitude'])



# df = pd.DataFrame(
#      split_df,
#      columns=['latitude', 'longitude'])

# st.map(df)

