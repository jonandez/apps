#!/bin/bash
# Delete prometheus app
echo -e "[TASK 1 ] Delete monitoring namespace"
kubectl delete namespace monitoring

# Create prometheus app
echo -e "\n[TASK 2 ] Kube State Metrics"
kubectl delete -f state/
