def is_sticker(update):
    result = False
    id = None
    sticker_pack = None

    if len(update)>6:
        if set(['attach1_type', 'attach1_product_id', 'attach1']).issubset(set(update[6].keys())):
            if update[6]['attach1_type'] == 'sticker':
                sticker_pack = update[6]['attach1_product_id']
                id = update[6]['attach1']
                result = True
    return [result, id, sticker_pack]
