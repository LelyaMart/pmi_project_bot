FROM python
COPY requirements.txt /requirements.txt
RUN pip install -Ur requirements.txt
RUN pip install -U scikit-image
RUN pip install -U dlib
COPY bot.py /bot.py
COPY dlib_face_recognition_resnet_model_v1.dat /dlib_face_recognition_resnet_model_v1.dat
COPY shape_predictor_68_face_landmarks.dat /shape_predictor_68_face_landmarks.dat
COPY teachers4.db /teachers4.db
COPY classification.py /classification.py
COPY dclass.py /dclass.py
CMD python bot.py
