from examples import Example
from injectable import injectable, InjectionContainer, Autowired, autowired


@injectable  # make examples also injectable for testing
class CyclicDependency(Example):
    @autowired
    def __init__(self, service_a: Autowired("A"), service_b: Autowired("B")):
        self.service_a = service_a
        self.service_b = service_b

    def run(self):
        print(self.service_a.message_b)
        print(self.service_b.message_a)


if __name__ == "__main__":
    InjectionContainer.load()
    example = CyclicDependency()
    example.run()