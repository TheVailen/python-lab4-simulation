from src.simulation import run_simulation

def main():
    print("=== ЗАПУСК СИМУЛЯЦИИ БИБЛИОТЕКИ ===")
    run_simulation(steps=15, seed=None)
    print("=== СИМУЛЯЦИЯ ЗАВЕРШЕНА ===")

if __name__ == "__main__":
    main()