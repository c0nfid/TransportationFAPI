from sqlalchemy import Sequence, RowMapping


def unpacking_map(maps: Sequence[RowMapping], *args: str):
    result: list[dict] = []
    for instance in maps:
        processed_instance = {}
        for model_name in args:
            processed_instance.update(
                dict(
                    filter(
                        lambda x: x[0][0] != "_", instance[model_name].__dict__.items()
                    )
                )
            )
        result.append(processed_instance)
    return result
