modules:
	pip install keyboard
	pip install grpcio
	pip install grpcio_tools

compile:
	python3 -m grpc_tools.protoc -I . --python_out=./build --pyi_out=./build --grpc_python_out=./build ./broker.proto