from __future__ import print_function

import logging

import grpc
import broker_pb2_grpc
import broker_pb2
import os
from Menu import Menu


def run():
    with grpc.insecure_channel("0.tcp.ngrok.io:18355") as channel:
        stub = broker_pb2_grpc.BrokerStub(channel)

        menu = Menu(stub)
        menu.start()
            
            

if __name__ == '__main__':
    logging.basicConfig()
    run()