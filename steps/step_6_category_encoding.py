import json
import pandas as pd

# 6
# koduje dane kategoryczne do liczb
def category_encoding(data, result_dir):
    # po kolei dla każdego pola
    print(f'(6) Encoding categories, will save files to: {result_dir}/')

    data['proto'] = data['proto'].astype('category')
    data['proto_id'] = data['proto'].cat.codes
    proto_map = dict(enumerate(data['proto'].cat.categories))

    data['service'] = data['service'].astype('category')
    data['service_id'] = data['service'].cat.codes
    service_map = dict(enumerate(data['service'].cat.categories))

    data['state'] = data['state'].astype('category')
    data['state_id'] = data['state'].cat.codes
    state_map = dict(enumerate(data['state'].cat.categories))

    data = data.drop(columns=['proto', 'service', 'state'])
    with open(f'{result_dir}/labels_proto.json', 'w') as f:
        json.dump(proto_map, f, indent=4)
    with open(f'{result_dir}/labels_service.json', 'w') as f:
        json.dump(service_map, f, indent=4)
    with open(f'{result_dir}/labels_state.json', 'w') as f:
        json.dump(state_map, f, indent=4)

    # zapisywanie, żeby widzieć wyniki z danego kroku
    data.to_csv(f'{result_dir}/result.csv', index=False)
    return data

# funkcje pomocnicze
