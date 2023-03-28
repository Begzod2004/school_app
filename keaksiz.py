
class InvoiceListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get(self, request):
        Invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(Invoices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class InvoiceRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get_object(self, pk):
        return get_object_or_404(Invoice, pk=pk)

    def get(self, request, pk):
        Invoice = self.get_object(pk)
        serializer = InvoiceSerializer(Invoice)
        return Response(serializer.data)

    def put(self, request, pk):
        Invoice = self.get_object(pk)
        serializer = InvoiceSerializer(Invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        Invoice = self.get_object(pk)
        Invoice.delete()
        return Response(status=204)
