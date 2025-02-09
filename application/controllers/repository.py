from application.models import Repository


class RepositoryController:
    def get_all_repositories(self):
        repositories = Repository.objects.all()
        return repositories

    def get_repositories_by_name(self, name: str) -> list[Repository]:
        repositories = Repository.objects.filter(name=name)
        return repositories

    def create_repository(self, data: dict) -> Repository:
        repository = Repository.objects.create(**data)
        return repository

    def update_repository(self, repository_id: str, data: dict) -> Repository:
        repository = Repository.objects.get(id=repository_id)
        repository.update(**data)
        return repository

    def delete_repository(self, repository_id: str) -> None:
        repository = Repository.objects.get(id=repository_id)
        repository.delete()
