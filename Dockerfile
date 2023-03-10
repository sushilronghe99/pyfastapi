FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9



WORKDIR /rembg

COPY . .

RUN python3.9 -m pip install .
RUN mkdir -p ~/.u2net
RUN wget https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2netp.onnx -O ~/.u2net/u2netp.onnx
RUN wget https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx -O ~/.u2net/u2net.onnx
RUN wget https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net_human_seg.onnx -O ~/.u2net/u2net_human_seg.onnx
RUN wget https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net_cloth_seg.onnx -O ~/.u2net/u2net_cloth_seg.onnx

EXPOSE 5000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "3000"]
