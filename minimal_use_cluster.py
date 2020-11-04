import ray

@ray.remote
def identity(x):
    return x

if __name__ == "__main__":
  ray.init(address='auto')
  future = identity.remote(0)
  ray.get([future])
  ray.shutdown()
