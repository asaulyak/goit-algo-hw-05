import timeit

from boyer_moore import boyer_moore_search
from kmp import kmp_search
from articles import article_1, article_2
from rabin_karp import rabin_karp_search

repeats = 10

article_1_exiting_pattern = 'Кожна система містить набір обмежень і вимог'
article_1_non_exiting_pattern = 'Параметри 2 серії експериментів'

article_2_exiting_pattern = 'Параметри 2 серії експериментів'
article_2_non_exiting_pattern = 'Кожна система містить набір обмежень і вимог'


kmp_art1_existing_execution_time = timeit.timeit(lambda: kmp_search(article_1, article_1_exiting_pattern), number=repeats)
print('KMP: article 1 with existing pattern', kmp_art1_existing_execution_time / repeats)

kmp_art1_non_existing_execution_time = timeit.timeit(lambda: kmp_search(article_1, article_1_non_exiting_pattern), number=repeats)
print('KMP: article 1 with non-existing pattern', kmp_art1_non_existing_execution_time / repeats)

kmp_art2_existing_execution_time = timeit.timeit(lambda: kmp_search(article_2, article_2_exiting_pattern), number=repeats)
print('KMP: article 2 with existing pattern', kmp_art2_existing_execution_time / repeats)

kmp_art2_non_existing_execution_time = timeit.timeit(lambda: kmp_search(article_2, article_2_non_exiting_pattern), number=repeats)
print('KMP: article 2 with non-existing pattern', kmp_art2_non_existing_execution_time / repeats)

print('===========================================================================================')

bm_art1_existing_execution_time = timeit.timeit(lambda: boyer_moore_search(article_1, article_1_exiting_pattern), number=repeats)
print('Boyer-Moore: article 1 with existing pattern', bm_art1_existing_execution_time / repeats)

bm_art1_non_existing_execution_time = timeit.timeit(lambda: boyer_moore_search(article_1, article_1_non_exiting_pattern), number=repeats)
print('Boyer-Moore: article 1 with non-existing pattern', bm_art1_non_existing_execution_time / repeats)

bm_art2_existing_execution_time = timeit.timeit(lambda: boyer_moore_search(article_2, article_2_exiting_pattern), number=repeats)
print('Boyer-Moore: article 2 with existing pattern', bm_art2_existing_execution_time / repeats)

bm_art2_non_existing_execution_time = timeit.timeit(lambda: boyer_moore_search(article_2, article_2_non_exiting_pattern), number=repeats)
print('Boyer-Moore: article 2 with non-existing pattern', bm_art2_non_existing_execution_time / repeats)

print('===========================================================================================')

rk_art1_existing_execution_time = timeit.timeit(lambda: rabin_karp_search(article_1, article_1_exiting_pattern), number=repeats)
print('Rabin-Karp: article 1 with existing pattern', rk_art1_existing_execution_time / repeats)

rk_art1_non_existing_execution_time = timeit.timeit(lambda: rabin_karp_search(article_1, article_1_non_exiting_pattern), number=repeats)
print('Rabin-Karp: article 1 with non-existing pattern', rk_art1_non_existing_execution_time / repeats)

rk_art2_existing_execution_time = timeit.timeit(lambda: rabin_karp_search(article_2, article_2_exiting_pattern), number=repeats)
print('Rabin-Karp: article 2 with existing pattern', rk_art2_existing_execution_time / repeats)

rk_art2_non_existing_execution_time = timeit.timeit(lambda: rabin_karp_search(article_2, article_2_non_exiting_pattern), number=repeats)
print('Rabin-Karp: article 2 with non-existing pattern', rk_art2_non_existing_execution_time / repeats)

print('===========================================================================================')

measures_art_1 = [
    (kmp_art1_existing_execution_time, 'KMP: Article 1, existing pattern'),
    (kmp_art1_non_existing_execution_time, 'KMP: Article 1, non-existing pattern'),
    (bm_art1_existing_execution_time, 'Boyer-Moore: Article 1, existing pattern'),
    (bm_art1_non_existing_execution_time, 'Boyer-Moore: Article 1, non-existing pattern'),
    (rk_art1_existing_execution_time, 'Rabin-Karp: Article 1, existing pattern'),
    (rk_art1_non_existing_execution_time, 'Rabin-Karp: Article 1, non-existing pattern'),

]

measures_art_2 = [
    (kmp_art2_existing_execution_time, 'KMP: Article 2, existing pattern'),
    (kmp_art2_non_existing_execution_time, 'KMP: Article 2, non-existing pattern'),
    (bm_art2_existing_execution_time, 'Boyer-Moore: Article 2, existing pattern'),
    (bm_art2_non_existing_execution_time, 'Boyer-Moore: Article 2, non-existing pattern'),
    (rk_art2_existing_execution_time, 'Rabin-Karp: Article 2, existing pattern'),
    (rk_art2_non_existing_execution_time, 'Rabin-Karp: Article 2, non-existing pattern'),
]

print('RESULTS')
print('Article 1:')

art_1_winner = sorted(measures_art_1, key=lambda item: item[0])[:1][0]
print(art_1_winner[1])

print('Article 2:')

art_2_winner = sorted(measures_art_2, key=lambda item: item[0])[:1][0]
print(art_2_winner[1])


print('General:')

measures = measures_art_1 + measures_art_2
winner = sorted(measures, key=lambda item: item[0])[:1][0]
print(winner[1])
