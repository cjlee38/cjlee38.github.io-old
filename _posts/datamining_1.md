
---
layout: post
title:  "# Java로 구현하는 연관규칙( feat. Apriori )"
date:   2100-01-01 00:00:00 +0900
categories: []
tags: 
---
```java
import com.google.common.collect.Sets;

import java.util.*;

public class Apriori {
    private Float minSupport;
    private Set<Set<String>> dataset;
    private Map<Set<String>, Float> result;

    public Apriori(Float minSupport, Set<Set<String>> dataset) {
        this.minSupport = minSupport;
        this.dataset = dataset;
        this.result = new HashMap<>();
    }

    public Map<Set<String>, Float> getResult() {
        return result;
    }

    public void run() {
        Set<String> itemset = createSet(dataset);
        Integer level = 1;
        Integer maxLevel = itemset.size();

        while (level < maxLevel) {
            if (level > 2) {
                break;
            }
            try {
                Set<Set<String>> combinations = getCombinations(itemset, level);
                Map<Set<String>, Float> supportedItemset = getSupportedItemset(combinations);
                result.putAll(supportedItemset);
                itemset = createSet(supportedItemset.keySet());
                level++;
            } catch (Exception e ) {
                break;
            }


            if (itemset.size() <= 1) {
                break;
            }
        }

    }

    public Set<Set<String>> getCombinations(Set<String> set, Integer level) {
        return Sets.combinations(set, level);
    }

    // 중복없는 데이터를 구하는 함수
    public Set<String> createSet(Set<Set<String>> data) {
        Set<String> set = new HashSet<>();
        for (Set<String> transaction : data) {
            for ( String item : transaction) {
                set.add(item);
            }
        }
        return set;
    }

    public Float calcSupport(Set<String> itemset) {
        Integer occurence = 0;
        for( Set<String> transaction : dataset) {
            if (transaction.containsAll(itemset)) {
                occurence++;
            }
        }
        return occurence / ((float)dataset.size());
    }

    public Map<Set<String>, Float> getSupportedItemset(Set<Set<String>> itemset) {
        Map<Set<String>, Float> map = new HashMap<>();
        for (Set<String> comb : itemset) {
            map.put(comb, calcSupport(comb));
        } // support 계산

        map.entrySet().removeIf(x -> x.getValue() < minSupport);

        return map;
    }
}
```