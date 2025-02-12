RATIO_TOLERANCE = 0.005

def calculate_possible_pairs_in_ratio(target_ratio, max_item1):
    """Find item1/item2 pairs that approximate target_ratio up to max_item1."""
    try:
        target_ratio = round(target_ratio, 3)
        results = []
        best_saved_ratio = 0

        item1 = 1
        item2 = 1

        while item2 <= max_item1:
            current_ratio = round(item2 / item1, 4)

            if abs(target_ratio - current_ratio) == 0:
                result = {'ratio': current_ratio, 'x1': item1, 'x2': item2}
                results.append(result)
                if item2 <= max_item1 / 2:
                    multiplier = max_item1 // item2
                    result2 = result.copy()
                    result2['x1'] = item1 * multiplier
                    result2['x2'] = item2 * multiplier
                    result2['ratio'] = current_ratio
                    results.append(result2)
                return results

            elif (abs(target_ratio - current_ratio) < abs(target_ratio - best_saved_ratio)
                  and abs(target_ratio - current_ratio) < RATIO_TOLERANCE
                  and (item1 % 2 == 1 or item2 % 2 == 1)):
                results.append({'ratio': current_ratio, 'x1': item1, 'x2': item2})
                best_saved_ratio = current_ratio

            if current_ratio < target_ratio:
                item2 += 1
            else:
                item1 += 1

        return results
    except Exception as e:
        return e


def get_item_ratio(v1, v2):
    """Return the value if the other parameter is 1."""
    if v1 == 1:
        return v2
    elif v2 == 1:
        return v1
    else:
        raise ValueError("One of the inputs must be equal to 1.")


def cut_exceeding_results(thresh, data):
    """Cut off data where x1 > thresh."""
    for idx, item in enumerate(data):
        if item['x1'] > thresh:
            return data[:idx]
    return data


def calculate_full_exchange(buy_ratio_item1, buy_ratio_item2,
                            sell_ratio_item1, sell_ratio_item2,
                            total_item1):
    buy_val = get_item_ratio(buy_ratio_item1, buy_ratio_item2)
    buy_data = calculate_possible_pairs_in_ratio(buy_val, total_item1)

    sell_val = get_item_ratio(sell_ratio_item1, sell_ratio_item2)
    sell_data = calculate_possible_pairs_in_ratio(sell_val, total_item1)

    cut_buy = cut_exceeding_results(total_item1, buy_data)
    cut_sell = cut_exceeding_results(total_item1, sell_data)

    profit = round(sell_val * total_item1 - buy_val * total_item1, 2)
    return cut_buy, cut_sell, profit


def calculate_buy_proportions_only(buy_ratio_item1, buy_ratio_item2, total_item1):
    buy_val = get_item_ratio(buy_ratio_item1, buy_ratio_item2)
    return calculate_possible_pairs_in_ratio(buy_val, total_item1)
