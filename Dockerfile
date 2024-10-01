# Use the official lightweight Python image.

FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the add_meta_tags.py script
COPY add_meta_tags.py .

# Run the script to add meta tags
RUN python add_meta_tags.py

# Copy the rest of the application code into the container
COPY . .

# Expose the port Streamlit runs on
EXPOSE 8000

# Set the PATH environment variable to include /usr/local/bin
ENV PATH="/usr/local/bin:${PATH}"

# Debugging steps
RUN which streamlit
RUN echo $PATH

# Run the application
CMD ["/usr/local/bin/streamlit", "run", "src/streamlit_app.py", "--server.port=8000", "--server.address=0.0.0.0"]






