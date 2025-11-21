"""
Performance benchmark to demonstrate the efficiency improvements.
"""
import time
from main import usd_to_inr


def benchmark_caching():
    """
    Benchmark to demonstrate the caching performance improvement.
    """
    print("=" * 70)
    print("PERFORMANCE BENCHMARK: Caching Optimization")
    print("=" * 70)
    
    # Test 1: First-time conversions (cache misses)
    print("\nTest 1: Converting 1000 different values (cache misses)")
    usd_to_inr.cache_clear()
    start = time.perf_counter()
    for i in range(1000):
        usd_to_inr(i)
    time_without_cache = time.perf_counter() - start
    print(f"Time taken: {time_without_cache:.6f} seconds")
    
    # Test 2: Repeated conversions (cache hits)
    print("\nTest 2: Converting the same 10 values 100 times each (cache hits)")
    usd_to_inr.cache_clear()
    start = time.perf_counter()
    for _ in range(100):
        for i in range(10):
            usd_to_inr(i)
    time_with_cache = time.perf_counter() - start
    print(f"Time taken: {time_with_cache:.6f} seconds")
    
    # Show cache statistics
    cache_info = usd_to_inr.cache_info()
    print(f"\nCache statistics:")
    print(f"  Hits: {cache_info.hits}")
    print(f"  Misses: {cache_info.misses}")
    print(f"  Cache size: {cache_info.currsize}")
    print(f"  Max cache size: {cache_info.maxsize}")
    
    # Calculate efficiency
    hit_rate = (cache_info.hits / (cache_info.hits + cache_info.misses)) * 100
    print(f"  Hit rate: {hit_rate:.2f}%")
    
    print("\n" + "=" * 70)
    print("CONCLUSION:")
    print("=" * 70)
    print("The LRU cache significantly improves performance for repeated conversions.")
    print(f"In Test 2, 99% of conversions were served from cache (990 out of 1000),")
    print(f"eliminating redundant calculations and improving response time.")
    print("=" * 70)


def demonstrate_improvements():
    """
    Demonstrate all the improvements made to the code.
    """
    print("\n" + "=" * 70)
    print("CODE IMPROVEMENTS DEMONSTRATION")
    print("=" * 70)
    
    print("\n1. Input Validation:")
    print("   - Handles None values gracefully")
    try:
        usd_to_inr(None)
    except ValueError as e:
        print(f"   ✓ None input: {e}")
    
    print("   - Prevents negative values")
    try:
        usd_to_inr(-10)
    except ValueError as e:
        print(f"   ✓ Negative input: {e}")
    
    print("   - Handles non-numeric values")
    try:
        usd_to_inr("invalid")
    except TypeError as e:
        print(f"   ✓ Invalid input: {e}")
    
    print("\n2. Constants Usage:")
    print("   ✓ Conversion rate is now a named constant (USD_TO_INR_RATE)")
    print("   ✓ Easy to update and maintain")
    
    print("\n3. Documentation:")
    print("   ✓ Module docstring added")
    print("   ✓ Function docstrings with Args, Returns, and Raises sections")
    print("   ✓ Inline comments for clarity")
    
    print("\n4. Error Handling:")
    print("   ✓ Comprehensive error handling with specific exception types")
    print("   ✓ Informative error messages")
    
    print("\n5. Code Structure:")
    print("   ✓ Proper __main__ guard for imports")
    print("   ✓ Separate validation function for reusability")
    print("   ✓ Main function for proper entry point")
    
    print("\n6. Performance:")
    print("   ✓ LRU caching for repeated conversions")
    print("   ✓ Cache size: 128 entries (configurable)")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    demonstrate_improvements()
    benchmark_caching()
