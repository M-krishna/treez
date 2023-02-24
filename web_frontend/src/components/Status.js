export const Status = ({status}) => {
  /*
  Custom component used for showing the status of the transactions.
  */

  const COLORS = {
    'Common': {
      padding: '6px', borderRadius: '2px', fontWeight: 'bold', fontSize: 'medium'
    },
    'Returned': {
      backgroundColor: '#eeaeae',
      color: '#f01e1e',
    },
    'Successful': {
      backgroundColor: '#98d998',
      color: '#156f1e'
    },
    'Authorized': {
      backgroundColor: '#f6f68f',
      color: '#282c08'
    },
    'Cancelled': {
      backgroundColor: '#e0e0e0',
      color: '#040403'
    },
    'Initiated': {
      backgroundColor: '#a3cdf6',
      color: '#0f1ac4',
    }
  }

  return (
    <div style={{...COLORS[status], ...COLORS['Common']}}>
      {status}
    </div>
  )
}