A, B, C, X = map(int, input().split())  

# Calculate the volumes
cuboid_volume = A * B * C
cube_volume = X * X * X

# Compare volumes and print the result
if cuboid_volume > cube_volume:
  print("Cuboid")
elif cube_volume > cuboid_volume:
  print("Cube")
else:
  print("Equal")
