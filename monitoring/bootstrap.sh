#!/bin/bash
# Create prometheus app
echo "[TASK 1 ] Create Prometheus app"
kubectl create namespace monitoring
kubectl apply -f prometheus/


# Create prometheus app
echo -e "\n[TASK 2 ] Kube State Metrics"
kubectl apply -f state/


echo -e "\n[TASK 2 ] Create Grafana app"
kubectl apply -f grafana/