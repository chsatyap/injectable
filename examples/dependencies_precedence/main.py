from examples import Example
from examples.dependencies_precedence.services.abstract_service import AbstractService
from injectable import injectable, InjectionContainer, autowired, Autowired


@injectable  # make examples also injectable for testing
class DependenciesPrecedence(Example):
    @autowired
    def __init__(
        self,
        sum_service: Autowired(AbstractService),
        multiply_service: Autowired("multiply"),
    ):
        self.sum_service = sum_service
        self.multiply_service = multiply_service

    def run(self):
        print(self.sum_service.combine(7, 7))
        print(self.multiply_service.combine(7, 7))


if __name__ == "__main__":
    InjectionContainer.load()
    example = DependenciesPrecedence()
    example.run()