import './App.css'
import axios from "axios";
import moment from "moment/moment";
import { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import { MultiSelect } from "react-multi-select-component";
import { getTransactions, searchTransactions, filterTransactions, getTransactionsWithPage, getStatus } from './services';
import { InputTextStyles, SelectFieldStyles, tableHeaderStyles } from './styles/styles';
import {Status} from './components/Status';


const columns = [
    {
        name: 'DATE',
        selector: row => row.date,
        format: row => moment(row.date).format('MMMM D, h:m a')
    },
    {
        name: 'GROSS AMOUNT',
        selector: row => row.gross_amount,
        format:  row => `$${row.gross_amount}`
    },
    {
      name: 'STATUS',
      selector: row => row.status,
      cell: row => <Status status={row.status} />
    },
    {
      name: 'CUSTOMER',
      selector: row => row.customer
    },
    {
      name: 'SWIFTER ID',
      selector: row => row.swifter_id
    },
    {
      name: 'EXTERNAL ID',
      selector: row => row.external_id
    },
    {
      name: 'SOURCE',
      selector: row => row.source
    }
];

function App() {

  const [transactions, setTransactions] = useState({});
  const [selected, setSelected] = useState([]);
  const [statusIds, setStatusIds] = useState('');
  const [status, setStatus] = useState('');

  useEffect(() => {
    getStatus(setStatus)
    getTransactions(setTransactions)
  }, []);

  const handlePageChange = async (page) => {
      getTransactionsWithPage(page, selected, statusIds, setTransactions)
  };

  const handleSearch = async (e) => {
    searchTransactions(e.target.value, setTransactions)
  }

  const handleSelected = async (e) => {
    let status_ids = '';
    for (let i of e) {
      if(status_ids === ''){
        status_ids += `${String(i.id)}`
      } else {
        status_ids += `,${String(i.id)}`
      }
    }
    setSelected(e)
    setStatusIds(status_ids)
    filterTransactions(status_ids, setTransactions)
  }


  return (
    <>
      <div id="header" style={{marginBottom: '70px'}}>
        <h2 style={{margin: '0'}}>Transactions</h2>
        <span>View summary and details of your transactions here</span>
      </div>
      <div id="data-table" style={{zIndex: '0'}}>
        {transactions && status &&
          <>
          <div style={tableHeaderStyles}>
            <input 
              type="text" 
              onChange={handleSearch} 
              placeholder="Search by customer name..."
              style={InputTextStyles}
            />
            <MultiSelect 
              options={status.results}
              value={selected}
              onChange={handleSelected}
              labelledBy={"Filter"}
              style={SelectFieldStyles}
            />
          </div>
          <DataTable 
            columns={columns} 
            data={transactions.results} 
            pagination
            paginationServer  
            paginationPerPage={15}
            paginationTotalRows={transactions?.count}
    		    onChangePage={handlePageChange}
            persistTableHead
            fixedHeader
            fixedHeaderScrollHeight='400px'
            striped
            highlightOnHover
            responsive
          />
          </>
        }
      </div>
    </>
  );
}

export default App;
