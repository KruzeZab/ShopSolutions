import { ChakraProvider } from "@chakra-ui/react";
import theme from "./theme";

const App = () => {
  return (
    <div>
      <ChakraProvider theme={theme}>App</ChakraProvider>
    </div>
  );
};

export default App;
