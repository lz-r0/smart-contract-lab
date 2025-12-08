// About: Simple snippet to read ETH balance via Web3.


const Web3 = require("web3");
const web3 = new Web3("https://mainnet.infura.io/v3/YOUR_KEY");

(async () => {
  const balance = await web3.eth.getBalance("0x...");
  console.log(web3.utils.fromWei(balance, "ether"));
})();


// Infura: hosted Ethereum node service.
// async: lets JS wait for network calls without blocking.
// EVM: virtual machine that runs all Ethereum smart contracts.
