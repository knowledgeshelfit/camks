import cv2
import streamlit as st

from streamlit_webrtc import (
    AudioProcessorBase,
    RTCConfiguration,
    VideoProcessorBase,
    WebRtcMode,
    webrtc_streamer,
)


RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)


def main():
    st.header("WebRTC demo")
    
    programatically_control_page = "Control the playing state programatically"
    app_mode = st.sidebar.selectbox(
        "Choose the app mode",
        [
            programatically_control_page,
        ],
    )
    st.subheader(app_mode)

    
    if app_mode == programatically_control_page:
        app_programatically_play()


def app_programatically_play():
    """ A sample of controlling the playing state from Python. """
    playing = st.checkbox("Playing", value=True)

    webrtc_streamer(
        key="media-constraints",
        desired_playing_state=playing,
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
    )


if __name__ == "__main__":
    main()
