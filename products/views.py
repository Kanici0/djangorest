from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import (DirectorSerializer, DirectorDetailSerializer,
                          MovieSerializer, MovieDetailSerializer, ReviewSerializer, ReviewDetailSerializer,
                          MoviesReviewsSerializer)


@api_view(['GET'])
def director_api_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data=data)


@api_view(['GET', 'POST'])
def director_list_create_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        serializer = DirectorDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response({'error': 'Director not found!'}, status=status.HTTP_404_NOT_FOUND)

    data = DirectorDetailSerializer(director).data
    return Response(data=data)


@api_view(['GET'])
def movie_api_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = MovieDetailSerializer(movie).data
        return Response(data=data)

    elif request.method == 'PUT':
        serializer = MovieDetailSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def review_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data=data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response({'error': 'Review not found!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = ReviewDetailSerializer(review).data
        return Response(data=data)

    elif request.method == 'PUT':
        serializer = ReviewDetailSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def movies_reviews_api_view(request):
    movies = Movie.objects.all()
    data = MoviesReviewsSerializer(movies, many=True).data
    return Response(data=data)
