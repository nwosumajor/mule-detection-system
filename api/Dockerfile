# Use the official Google TensorFlow image (already has TF 2.16 installed!)
FROM tensorflow/tensorflow:latest

# Set the working directory
WORKDIR /app

# Copy and install the remaining lightweight dependencies
COPY requirements.txt .

# THE FIX: Force pip to override the OS-level blinker package first
RUN pip install --no-cache-dir --ignore-installed blinker

# Now install the rest of your web API requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy your scripts and ML artifacts
COPY app.py .
COPY mule_detection_model.keras .
COPY scaler.pkl .

# Expose the API port
EXPOSE 5000

# Launch the API
CMD ["python", "app.py"]
