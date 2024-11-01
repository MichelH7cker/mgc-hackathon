// ResponseContext.js
import React, { createContext, useState } from 'react';

// Cria o contexto
export const ResponseContext = createContext();

// Cria o provider para envolver componentes e compartilhar o estado
export const ResponseProvider = ({ children }) => {
    const [responseData, setResponseData] = useState(null); // Estado para armazenar a resposta da API

    return (
        <ResponseContext.Provider value={{ responseData, setResponseData }}>
            {children}
        </ResponseContext.Provider>
    );
};
