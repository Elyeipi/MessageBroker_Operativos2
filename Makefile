modules:
	pip install --upgrade pip
	pip install keyboard
	pip install grpcio
	pip install grpcio_tools

compile-grpc-python:
	python -m grpc_tools.protoc -I . --python_out=./build --pyi_out=./build --grpc_python_out=./build ./broker.proto

compile-grpc-python3:
	python3 -m grpc_tools.protoc -I . --python_out=./build --pyi_out=./build --grpc_python_out=./build ./broker.proto