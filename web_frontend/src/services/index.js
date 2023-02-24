import axios from "axios";

const BASE_URL = 'http://localhost:8000'

export const getTransactions = (setTransactions) => {
    const URL = BASE_URL + '/transactions/'
    axios.get(URL)
        .then(res => setTransactions(res.data))
        .catch(err => console.error(err))
}

export const searchTransactions = (name, setTransactions) => {
    const URL = BASE_URL + `/transactions/?search=${name}`
    axios.get(URL)
        .then(res => setTransactions(res.data))
        .catch(err => console.error(err))
}

export const filterTransactions = (status_ids, setTransactions) => {
    const URL = BASE_URL + `/transactions/?status=${status_ids}`
    axios.get(URL)
        .then(res => setTransactions(res.data))
        .catch(err => console.error(err))
}

export const getTransactionsWithPage = (page, selected, statusIds, setTransactions) => {
    let URL = BASE_URL + `/transactions/?page=${page}`
    if(selected.length > 0) {
        URL += `&status=${statusIds}`
    }
    axios.get(URL)
        .then(res => setTransactions(res.data))
        .catch(err => console.error(err))
}

export const getStatus = (setStatus) => {
    const URL = BASE_URL + `/transactions/status`
    axios.get(URL)
        .then(res => setStatus(res.data))
        .catch(err => console.error(err))
}