from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from restaurantes.serializers import RestaurantSerializer
from restaurantes.models import Restaurants

@api_view(['GET','POST'])
def restaurants_api_view(request):
    
    # List
    if request.method == 'GET':
        restaurant = Restaurants.objects.all()
        restaurant_serializer = RestaurantSerializer(restaurant,many = True)
        return Response(restaurant_serializer.data, status = status.HTTP_200_OK)
    
    # Create
    elif request.method == 'POST':
        restaurant_serializer = RestaurantSerializer(data=request.data)
        if restaurant_serializer.is_valid():
            restaurant_serializer.save()
            #return Response(restaurant_serializer.data, status = status.HTTP_201_CREATED)
            return Response({'message':'Usuario creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(restaurant_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def restaurant_detail_view(request,pk):
    restaurant = Restaurants.objects.filter(id = pk).first()
    
    if restaurant:
        
        # Retrieve
        if request.method == 'GET':
            restaurant_serializer = RestaurantSerializer(restaurant)
            return Response(restaurant_serializer.data, status = status.HTTP_200_OK)
        
        # Update
        elif request.method == 'PUT':
            restaurant_serializer = RestaurantSerializer(restaurant, data=request.data)
            print(restaurant_serializer.is_valid())

            # Validate
            if restaurant_serializer.is_valid():
                restaurant_serializer.save()
                #return Response(restaurant_serializer.data, status = status.HTTP_200_OK)
                return Response({'message':'Usuario actualizado correctamente'}, status = status.HTTP_200_OK)
            return Response(restaurant_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        # Delete
        elif request.method == 'DELETE':
            restaurant.delete()
            return Response({'message':'Usuario eliminado'}, status = status.HTTP_200_OK)
        
    return Response({'message':'No se ha encontrado el usuario'}, status = status.HTTP_400_BAD_REQUEST)