from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer, VendorPerformanceSerializer

class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_url_kwarg = 'vendor_id'

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_url_kwarg = 'po_id'

class VendorPerformanceAPIView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer
    lookup_url_kwarg = 'vendor_id'

    def retrieve(self, request, *args, **kwargs):
        vendor = self.get_object()
        performance_metrics = {
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'average_response_time': vendor.average_response_time,
            'fulfillment_rate': vendor.fulfillment_rate
        }
        return Response(performance_metrics)

class AcknowledgePurchaseOrderAPIView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_url_kwarg = 'po_id'

    def update(self, request, *args, **kwargs):
        # This method will handle PUT and PATCH requests, so we don't need to modify it.
        # However, we need to override the post method to handle POST requests.

        # Delegate the handling of POST requests to the update method
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Retrieve the PurchaseOrder instance
        instance = self.get_object()

        # Update the acknowledgment_date to the current time
        instance.acknowledgment_date = timezone.now()
        instance.save()

        # Recalculate average_response_time
        instance.vendor.update_average_response_time()

        # Construct the response message
        response_data = {
            'message': 'Purchase order acknowledged successfully.',
            'acknowledgment_date': instance.acknowledgment_date,  # Include acknowledgment_date in the response
            'trigger': 'Average response time will be recalculated.'  # Add trigger for the recalculation of average_response_time
        }

        # Return the response with the custom message and acknowledgment_date
        return Response(response_data, status=status.HTTP_200_OK)